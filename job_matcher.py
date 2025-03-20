import os
import requests
from dotenv import load_dotenv
from openai import OpenAI
from bs4 import BeautifulSoup

def main():
    # Load environment variables from a .env file
    load_dotenv(override=True)
    api_key = os.getenv('OPENAI_API_KEY')

    # Define headers for the HTTP requests
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
    }

    class Website:
        def __init__(self, url):
            """Create this Website object from the given URL using BeautifulSoup"""
            self.url = url
            # Check if the URL is a LinkedIn page
            if "linkedin.com" not in self.url:
                print("Error: The URL must be a LinkedIn page.")
                self.text = ""
                self.title = ""
            else:
                # Fetch the page content
                response = requests.get(url, headers=headers)
                soup = BeautifulSoup(response.content, 'html.parser')
                # Extract the title of the page
                self.title = soup.title.string if soup.title else "No title found"
                # Remove irrelevant tags from the body
                for irrelevant in soup.body(["script", "style", "img", "input"]):
                    irrelevant.decompose()
                # Extract the text content of the page
                self.text = soup.body.get_text(separator="\n", strip=True)

    # Define the system prompt for the OpenAI model
    system_prompt = (
        "You are a recruitment assistant specialized in evaluating candidates based on job offers. "
        "Your goal is to analyze candidate profiles and compare them with the job requirements to generate a useful summary for recruiters. "
        "Compare the job requirements with the candidate's experience and generate a list of strengths and gaps. Identify matches as strengths. "
        "Detect missing qualifications as gaps. Calculate a suitability score out of 10 based on alignment with the requirements.\n"
        "Only return the list of strengths and gaps and the score with a short justification."
    )

    def evaluate_candidates(offer_url, candidate_url):
        # Initialize the OpenAI API client
        openai = OpenAI()
        # Create Website objects for the job offer and candidate profile
        lnOffer = Website(offer_url)
        lnProfile = Website(candidate_url)

        # Check if the pages were processed successfully
        if not lnOffer.text or not lnProfile.text:
            print("Error: One or both pages could not be processed.")
            return

        # Define the user prompt for the OpenAI model
        user_prompt = (
            f"You are looking at the job offer titled '{lnOffer.title}'.\n\n"
            f"The content of the job offer is as follows:\n{lnOffer.text}\n"
            f"The candidate you are evaluating is {lnProfile.title}.\n\n"
            f"The content of the candidate's profile is as follows:\n{lnProfile.text}\n\n"
        )

        # Get the response from the OpenAI model
        response = openai.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ]
        )
        # Return the content of the response
        return response.choices[0].message.content

    # User input for URLs
    offer_url = input("Offer URL: ")
    candidate_url = input("Candidate URL: ")
    
    # Print the evaluation result
    print(evaluate_candidates(offer_url, candidate_url))

if __name__ == "__main__":
    main()
