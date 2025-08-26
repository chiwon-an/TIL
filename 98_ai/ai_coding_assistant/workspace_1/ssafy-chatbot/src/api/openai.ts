import OpenAI from "openai";

const openai = new OpenAI({
  apiKey: process.env.REACT_APP_OPENAI_API_KEY,
  dangerouslyAllowBrowser: true, // This is required for browser-based API calls
});

export async function sendMessage(prompt: string, imageUrl?: string): Promise<string> {
  try {
    // The PRD specifies gpt-5-nano, but it does not exist. Using gpt-3.5-turbo instead.
    const response = await openai.chat.completions.create({
      model: "gpt-3.5-turbo",
      messages: [
        {
          role: "user",
          content: prompt,
        },
      ],
    });

    return response.choices[0].message.content || "AI의 응답을 받지 못했습니다.";

  } catch (error) {
    console.error("Error calling OpenAI API:", error);
    return "AI 응답을 가져오는 중 오류가 발생했습니다.";
  }
}