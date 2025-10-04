import { useState } from 'react';
import { Container, Title, Text, Textarea, Button, Paper, Loader } from '@mantine/core';
import ReactMarkdown from 'react-markdown';

function App() {
  const [code, setCode] = useState('');
  const [review, setReview] = useState('');
  const [isLoading, setIsLoading] = useState(false);

  const handleReview = async () => {
    setIsLoading(true);
    setReview('');

    // Make sure this URL is correct from your "PORTS" tab for Port 8000
    const backendUrl = 'https://cuddly-carnival-69vw97wpxv9rh44gj-8000.app.github.dev';

    try {
      const response = await fetch(`${backendUrl}/review-code`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          code: code,
          language: 'python',
        }),
      });
      const data = await response.json();
      if (data.review) {
        setReview(data.review);
      } else {
        setReview(`Error: ${data.error || 'Unknown error'}`);
      }
    } catch (error) {
      setReview(`Failed to connect to the server. Is it running?`);
    }
    setIsLoading(false);
  };

  return (
    <Container size="md" my="xl">
      <Title order={1} align="center" mb="lg">
        CodeGuardian AI 🛡️
      </Title>
      <Text align="center" c="dimmed" mb="xl">
        Paste your code below to get an instant review from our AI assistants.
      </Text>

      <Textarea
        label="Your Code"
        placeholder="def hello_world(): ..."
        value={code}
        onChange={(event) => setCode(event.currentTarget.value)}
        minRows={10}
        autosize
      />

      <Button onClick={handleReview} fullWidth mt="md" disabled={isLoading || !code}>
        {isLoading ? <Loader size="xs" color="white" /> : 'Review Code'}
      </Button>

      {review && !isLoading && (
        <Paper withBorder p="md" mt="xl">
          <ReactMarkdown>{review}</ReactMarkdown>
        </Paper>
      )}

      {isLoading && (
         <Container align="center" p="xl">
            <Loader />
            <Text size="sm" mt="sm">AI is thinking...</Text>
        </Container>
      )}
    </Container>
  );
}

export default App;
