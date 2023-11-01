import { useState } from "react";

export default function Home() {
    const [query, setQuery] = useState("");
    const [results, setResults] = useState({ title: "", steps: [] });
    const [loading, setLoading] = useState(false);
    const [showResults, setShowResults] = useState(false);

    const fetchResults = async () => {
        setLoading(true);
        setShowResults(false);
        try {
            const response = await fetch(
                `http://localhost:8000/query?query=${query}`
            );
            const data = await response.json();
            setResults(data);
            setLoading(false);
            setShowResults(true);
        } catch (error) {
            console.error("Error fetching data:", error);
            setLoading(false);
        }
    };

    const handleQueryChange = (e) => {
        setQuery(e.target.value);
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        fetchResults();
    };

    return (
        <div className="container">
            <Navbar />
            {loading ? (
                <p>Loading...</p>
            ) : showResults ? (
                <ResultsList title={results.title} steps={results.steps} />
            ) : (
                <MainContent
                    query={query}
                    onQueryChange={handleQueryChange}
                    onSubmit={handleSubmit}
                />
            )}
            <Footer />
        </div>
    );
}

const Navbar = () => (
    <div id="navbar">
        <a href="/">Home</a>
        <a href="/about">About</a>
        <a href="/development">Development</a>
    </div>
);

const MainContent = ({ query, onQueryChange, onSubmit, results }) => (
    <div id="main-content">
        <SearchForm
            query={query}
            onChange={onQueryChange}
            onSubmit={onSubmit}
        />
        {results && results.title && (
            <ResultsList title={results.title} steps={results.steps} />
        )}
    </div>
);

const SearchForm = ({ query, onChange, onSubmit }) => (
    <form onSubmit={onSubmit}>
        <input
            type="text"
            id="query"
            name="query"
            placeholder="How to:"
            value={query}
            onChange={onChange}
        />
        <input type="submit" value="Submit" />
    </form>
);

const ResultsList = ({ title, steps }) => (
    <div>
        <h1>{title}</h1>
        <ul>
            {steps.map((item, index) => (
                <li key={index}>
                    {item.instruction}
                    <img
                        src={`data:image/png;base64,${item.image_path}`}
                        alt={`Image for ${item.instruction}`}
                    />
                </li>
            ))}
        </ul>
    </div>
);

const Footer = () => (
    <footer>
        <div className="container">
            <p>How To Dummies</p>
            <p>&copy; 2023 Your Company Name. All rights reserved.</p>
        </div>
    </footer>
);
