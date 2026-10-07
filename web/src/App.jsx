import { useState } from "react";

function App() {
    const [question, setQuestion] = useState("");
    const [answer, setAnswer] = useState("");
    const [sources, setSources] = useState([]);
    const [loading, setLoading] = useState(false);

    const askQuestion = async () => {
        if (!question.trim()) return;

        setLoading(true);

        try {
            const response = await fetch(
                "http://127.0.0.1:8000/api/ask",
                {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json"
                    },
                    body: JSON.stringify({
                        question: question
                    })
                }
            );

            const data = await response.json();

            setAnswer(data.answer);
            setSources(data.sources);
        } catch (error) {
            console.error(error);
            setAnswer("Unable to get an answer.");
        } finally {
            setLoading(false);
        }
    };

    return (
        <div>
            <h1>Health Policy Assistant</h1>

            <input
                value={question}
                onChange={(e) => setQuestion(e.target.value)}
                placeholder="Ask a question..."
            />

            <button onClick={askQuestion}>
                {loading ? "Asking..." : "Ask"}
            </button>

            {answer && (
                <div>
                    <h2>Answer</h2>
                    <p>{answer}</p>
                </div>
            )}

            {sources.length > 0 && (
                <div>
                    <h2>Sources</h2>

                    {sources.map((source, index) => (
                        <div key={index}>
                            <p>
                                {source.source}
                            </p>
                        </div>
                    ))}
                </div>
            )}
        </div>
    );
}

export default App;