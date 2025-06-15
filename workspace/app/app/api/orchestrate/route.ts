import { NextResponse } from 'next/server';

export async function POST(request: Request) {
  console.log('API route /api/orchestrate reached.');
  try {
    const { prompt, agents, isFollowUp, brainstormingMethod } = await request.json();

    if (!prompt) {
      return NextResponse.json({ error: 'Prompt is required' }, { status: 400 });
    }

    // Prepare the request body for FastAPI
    const requestBody: any = { prompt };
    
    // Add agents if provided
    if (agents && agents.length > 0) {
      requestBody.agents = agents;
    }
    
    // Add follow-up flag if provided
    if (isFollowUp) {
      requestBody.is_follow_up = isFollowUp;
    }
    
    // Add brainstorming method if provided
    if (brainstormingMethod) {
      requestBody.brainstorming_method = brainstormingMethod;
    }

    // Call the FastAPI orchestrator endpoint
    console.log('Calling FastAPI endpoint: http://127.0.0.1:8000/run');
    console.log('Request body:', requestBody);
    
    const fastapiResponse = await fetch('http://127.0.0.1:8000/run', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(requestBody),
    });
    console.log(`FastAPI response status: ${fastapiResponse.status}, ok: ${fastapiResponse.ok}`);

    if (!fastapiResponse.ok) {
      console.log('FastAPI response not OK, attempting to parse error JSON.');
      try {
        const errorData = await fastapiResponse.json();
        console.error('FastAPI error:', errorData.detail);
        return NextResponse.json({ error: `Orchestrator API error: ${errorData.detail}` }, { status: fastapiResponse.status });
      } catch (jsonError) {
        console.error('Failed to parse FastAPI error response as JSON:', jsonError);
        const errorText = await fastapiResponse.text();
        console.error('FastAPI error response text:', errorText);
        return NextResponse.json({ error: `Orchestrator API returned non-JSON error: ${errorText.substring(0, 100)}...` }, { status: fastapiResponse.status });
      }
    }

    console.log('FastAPI response OK, attempting to parse response JSON.');
    const result = await fastapiResponse.json();
    console.log('FastAPI response:', result);

    // Assuming the FastAPI endpoint returns a JSON object with a 'response' key
    return NextResponse.json({ response: result.response });

  } catch (error: any) {
    console.error('Caught error processing prompt or calling FastAPI:', error);
    // Attempt to get more details if it's a TypeError related to fetch
    if (error instanceof TypeError) {
        console.error('Error details:', error.message);
    }
    return NextResponse.json({ error: `Internal Server Error: ${error.message || error}` }, { status: 500 });
  }
}