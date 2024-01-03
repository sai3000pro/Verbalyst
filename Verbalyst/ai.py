import vertexai
from vertexai.language_models import TextGenerationModel

def AIResponse(prompt):
    vertexai.init(project="strange-reducer-392221", location="us-central1")
    parameters = {
        "candidate_count": 1,
        "max_output_tokens": 1024,
        "temperature": 0.2,
        "top_p": 0.95,
        "top_k": 40
    }
    model = TextGenerationModel.from_pretrained("text-bison@001")
    response = model.predict(
        f"""You are a program that counts the number of filler words in a paragraph of text that was generated from a speech-to-text AI. If there are no filler words, compliment the user and tell them they are doing a fantastic job and that their speech was articulate and eloquent. If the number of filler words is between 1-5 inclusive, tell the user that they\\'re doing a good job but their speech still has room for improvement. If the number of filler words is greater than 5,  tell the user that they are doing ok with their speech and provide them with a tip to improve their speech.

    Count the number of stutters and provide feedback: I would like to uh do my clothes.
    Summary: You have stuttered only once, so keep up the great work! Your speech still has room for improvement, but don\\'t be discouraged!

    Count the number of stutters and provide feedback: I um would like to er see Dan Heng
    Summary: You have stuttered only twice! You\\'re almost there to the 0 stutter mark- don\\'t give up just yet! 

    Count the number of stutters and provide feedback: Please er uh um er show me your homework um thanks.
    Summary: You\\'ve stuttered a total of 5 times. There\\'s room for improvement, but be proud of your progress!

    Count the number of stutters and provide feedback: Now, um, I\\'m sure you\\'re all aware that, uh, challenges will, um, inevitably arise, and we must, um, confront them head-on. But, you know, it\\'s not just about, um, reacting to these, uh, challenges; it\\'s also about, um, embracing them as, um, opportunities for growth and, um, improvement.
    Summary: You\\'ve stuttered a total of 9 times. Don\\'t give up yet, practice makes perfect. Try pausing between phrases to give yourself more time to think and speak. 

    Count the number of stutters and provide feedback: In conclusion, let us remember that change is inherent to life itself. Our ability to embrace it with open minds and open hearts will determine our collective success. Together, we can navigate the complexities of change, emerging stronger and more resilient than before.
    Summary: You\\'ve stuttered ZERO times! Congratulations for your skills and efforts- you\\'ll surely nail this performance!

    Count the number of stutters and provide feedback: Thank you for your unwavering attention.
    Summary: You\\'ve stuttered ZERO times! Congratulations for your skills and efforts- Can\\'t wait to see you ace this speech!

    Count the number of stutters and provide feedback: Welcome to the world of Earth, where we have billions of uh people who are capable of murder and other sinful acts!
    Summary: You have stuttered only once, so keep up the great work! Your speech still has room for improvement, but don\\'t be discouraged!

    Count the number of stutters and provide feedback: {prompt}
    Summary:
    """,
        **parameters
    )
    return response.text

# lets me test stuff just in this file
if __name__ == "__main__":
    result = AIResponse("FUCK YOU er")
    print(result)