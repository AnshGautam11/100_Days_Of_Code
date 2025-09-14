import google.generativeai as genai

# Configure with your actual Gemini API key
genai.configure(api_key="Api Key")  # Replace with your real key

def generate_brand_name(business_type, business_work):
    prompt = f"Suggest a catchy and unique brand name for a business in {business_type} that focuses on {business_work}."

    # Use the proper model and method
    model = genai.GenerativeModel(model_name="models/gemini-1.5-flash")

    # Generate content
    response = model.generate_content(prompt)

    return response.text.strip()

def main():
    print("🚀 Welcome to the Gemini Brand Name Generator!\n")

    business_type = input("🔸 What type of business do you have? ")
    business_work = input("🔹 What does your business do specifically? ")

    brand_name = generate_brand_name(business_type, business_work)

    print(f"\n✨ Suggested Brand Name: {brand_name}")

if __name__ == "__main__":
    main()
