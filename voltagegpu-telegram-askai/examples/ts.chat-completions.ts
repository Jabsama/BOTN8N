/**
 * VoltageGPU API - Chat Completions Example (TypeScript/Node.js)
 * Non-streaming request to the chat completions endpoint
 * 
 * Usage:
 *   export VOLTAGE_API_KEY="your_api_key_here"
 *   npx ts-node ts.chat-completions.ts
 *   # or compile and run:
 *   tsc ts.chat-completions.ts && node ts.chat-completions.js
 */

interface Message {
  role: 'system' | 'user' | 'assistant';
  content: string;
}

interface ChatCompletionRequest {
  model: string;
  messages: Message[];
  stream: boolean;
  max_tokens?: number;
  temperature?: number;
}

interface ChatCompletionResponse {
  id: string;
  object: string;
  created: number;
  model: string;
  choices: Array<{
    index: number;
    message: Message;
    finish_reason: string;
  }>;
  usage?: {
    prompt_tokens: number;
    completion_tokens: number;
    total_tokens: number;
  };
}

class VoltageGPUClient {
  private apiKey: string;
  private baseUrl: string = 'https://api.voltagegpu.com';

  constructor(apiKey?: string) {
    this.apiKey = apiKey || process.env.VOLTAGE_API_KEY || '';
    if (!this.apiKey) {
      throw new Error(
        'API key not provided. Set VOLTAGE_API_KEY environment variable or pass apiKey to constructor'
      );
    }
  }

  async chatCompletion(
    messages: Message[],
    options: {
      model?: string;
      maxTokens?: number;
      temperature?: number;
    } = {}
  ): Promise<ChatCompletionResponse> {
    const {
      model = 'deepseek-ai/DeepSeek-R1-sgtest',
      maxTokens = 512,
      temperature = 0.7
    } = options;

    const payload: ChatCompletionRequest = {
      model,
      messages,
      stream: false,
      max_tokens: maxTokens,
      temperature
    };

    const response = await fetch(`${this.baseUrl}/v1/chat/completions`, {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${this.apiKey}`,
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(payload)
    });

    if (!response.ok) {
      const error = await response.text();
      throw new Error(`API request failed: ${response.status} - ${error}`);
    }

    return response.json();
  }

  extractContent(response: ChatCompletionResponse): string {
    return response.choices?.[0]?.message?.content || 'No response content found';
  }
}

async function main() {
  console.log('VoltageGPU Chat Completions Example (TypeScript)');
  console.log('-'.repeat(50));

  try {
    const client = new VoltageGPUClient();

    // Example 1: Simple coding question
    console.log('\nExample 1: Coding Assistant');
    console.log('-'.repeat(50));

    const messages: Message[] = [
      {
        role: 'system',
        content: 'You are a helpful coding assistant. Keep answers concise and include code when relevant.'
      },
      {
        role: 'user',
        content: 'Write a TypeScript function to validate email addresses'
      }
    ];

    console.log(`User: ${messages[1].content}\n`);
    console.log('Sending request to VoltageGPU API...\n');

    const response = await client.chatCompletion(messages);
    const content = client.extractContent(response);

    console.log('Assistant:');
    console.log(content);

    if (response.usage) {
      console.log('\nToken Usage:');
      console.log(`  Total: ${response.usage.total_tokens}`);
      console.log(`  Prompt: ${response.usage.prompt_tokens}`);
      console.log(`  Completion: ${response.usage.completion_tokens}`);
    }

    // Example 2: Multi-turn conversation about VoltageGPU
    console.log('\n' + '='.repeat(50));
    console.log('Example 2: VoltageGPU Expert');
    console.log('-'.repeat(50));

    const conversation: Message[] = [
      {
        role: 'system',
        content: 'You are an expert on VoltageGPU infrastructure and pricing.'
      },
      {
        role: 'user',
        content: 'What are the main advantages of VoltageGPU?'
      }
    ];

    console.log(`User: ${conversation[1].content}\n`);

    const response2 = await client.chatCompletion(conversation);
    const assistantResponse = client.extractContent(response2);

    console.log('Assistant:', assistantResponse);

    // Add assistant response to conversation
    conversation.push({
      role: 'assistant',
      content: assistantResponse
    });

    // Follow-up question
    conversation.push({
      role: 'user',
      content: 'How does the pricing compare to AWS or Google Cloud?'
    });

    console.log(`\nUser: ${conversation[conversation.length - 1].content}\n`);

    const response3 = await client.chatCompletion(conversation);
    console.log('Assistant:', client.extractContent(response3));

    // Example 3: Using different parameters
    console.log('\n' + '='.repeat(50));
    console.log('Example 3: Custom Parameters');
    console.log('-'.repeat(50));

    const creativeMessages: Message[] = [
      {
        role: 'system',
        content: 'You are a creative writer.'
      },
      {
        role: 'user',
        content: 'Write a haiku about GPU computing'
      }
    ];

    console.log(`User: ${creativeMessages[1].content}\n`);

    const creativeResponse = await client.chatCompletion(creativeMessages, {
      temperature: 0.9,  // Higher temperature for more creativity
      maxTokens: 100     // Shorter response for haiku
    });

    console.log('Assistant (high temperature = 0.9):');
    console.log(client.extractContent(creativeResponse));

  } catch (error) {
    console.error('Error:', error);
    process.exit(1);
  }
}

// Run the examples
if (require.main === module) {
  main().catch(console.error);
}

// Export for use as a module
export { VoltageGPUClient, Message, ChatCompletionRequest, ChatCompletionResponse };
