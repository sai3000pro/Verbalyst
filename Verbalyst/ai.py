import vertexai
from vertexai.language_models import TextGenerationModel

def AIResponse(prompt):
    vertexai.init(project="pragmatic-ruler-392220", location="us-central1")
    parameters = {
        "candidate_count": 1,
        "max_output_tokens": 256,
        "temperature": 0.2,
        "top_p": 0.8,
        "top_k": 40
    }
    model = TextGenerationModel.from_pretrained("text-bison@001")
    response = model.predict(
        f"""You are a program that counts the number of filler words in a paragraph of text that was generated from a speech-to-text AI. If there are no filler words, compliment the user and tell them they are doing a fantastic job and that their speech was articulate and eloquent. If the number of filler words is between 1-5 inclusive, tell the user that they\'re doing a good job but their speech still has room for improvement. If the number of filler words is greater than 5,  tell the user that they are doing ok with their speech and provide them with a tip to improve their speech.

    input: I would like to uh do my clothes.
    output: I would like to uh do my clothes. \nYou have stuttered only once, so keep up the great work! Your speech still has room for improvement, but don\'t be discouraged!

    input: I um would like to er see Dan Heng
    output: I um would like to er see Dan Heng \nYou have stuttered only twice! You\'re almost there to the 0 stutter mark- don\'t give up just yet! 

    input: Please er uh um er show me your homework um thanks.
    output: Please er uh um er show me your homework um thanks. \nYou\'ve stuttered a total of 5 times. There\'s room for improvement, but be proud of your progress!

    input: Ladies and gentlemen, I stand before you today, um, to address a topic of, uh, great significance and, um, importance. We live in a world, um, where change is, you know, inevitable and, uh, constant. It\'s crucial for us, um, as a society, to, uh, come together and, um, adapt to these, uh, ever-evolving circumstances.


    output: Ladies and gentlemen, I stand before you today, um, to address a topic of, uh, great significance and, um, importance. We live in a world, um, where change is, you know, inevitable and, uh, constant. It\'s crucial for us, um, as a society, to, uh, come together and, um, adapt to these, uh, ever-evolving circumstances. \nYou\'ve stuttered a total of 9 times. Don\'t give up yet, practice makes perfect. Try taking in a deep breath before you start to speak to get the ball rolling.

    input: Now, um, I\'m sure you\'re all aware that, uh, challenges will, um, inevitably arise, and we must, um, confront them head-on. But, you know, it\'s not just about, um, reacting to these, uh, challenges; it\'s also about, um, embracing them as, um, opportunities for growth and, um, improvement.
    output: Now, um, I\'m sure you\'re all aware that, uh, challenges will, um, inevitably arise, and we must, um, confront them head-on. But, you know, it\'s not just about, um, reacting to these, uh, challenges; it\'s also about, um, embracing them as, um, opportunities for growth and, um, improvement. \nYou\'ve stuttered a total of 9 times. Don\'t give up yet, practice makes perfect. Try pausing between phrases to give yourself more time to think and speak. 

    input: In conclusion, let us remember that change is inherent to life itself. Our ability to embrace it with open minds and open hearts will determine our collective success. Together, we can navigate the complexities of change, emerging stronger and more resilient than before.
    output: In conclusion, let us remember that change is inherent to life itself. Our ability to embrace it with open minds and open hearts will determine our collective success. Together, we can navigate the complexities of change, emerging stronger and more resilient than before. \nYou\'ve stuttered ZERO times! Congratulations for your skills and efforts- you\'ll surely nail this performance!

    input: Thank you for your unwavering attention.
    output: Thank you for your unwavering attention. \nYou\'ve stuttered ZERO times! Congratulations for your skills and efforts- Can\'t wait to see you ace this speech!

    input: Welcome to the world of Earth, where we have billions of people who are capable of murder and other sinful acts!
    output: Welcome to the world of Earth, where we have billions of people who are capable of murder and other sinful acts! \nYou\'ve stuttered ZERO times! Congratulations for your skills and efforts- you seem to have quite

    input: {prompt}

    output:
    """,
        **parameters
    )
    return (response.text)

