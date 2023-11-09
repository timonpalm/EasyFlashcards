"use client";
import React, { useState } from 'react'
import utilStyles from './page.module.css';

export default function Home() {
  const [isLoading, setIsLoading] = useState(false)
  const [error, setError] = useState(null)
  const [response, setResponse] = useState(null)

  function download(filename, text) {
    const element = document.createElement("a");
    const file = new Blob([text], {type: 'text/plain'});
    element.href = URL.createObjectURL(file);
    element.download = filename;
    document.body.appendChild(element); // Required for this to work in FireFox
    element.click();
  }

  async function onSubmit(e) {
    e.preventDefault();
    setIsLoading(true);
    setError(null)
    setResponse(null)

    const formData = new FormData(e.currentTarget);
    console.log(formData.get('text'));

    try {
      const response = await fetch('http://localhost:5000/?key=5HA374PKTeDpEf7HXGNAz4qL9Vg9Ay246T4r25qY', {
        method: 'POST',
        body: formData,
      })

      // const data = "Juhuu it works!"
 
      if (!response.ok) {
        throw new Error('Failed to submit the data. Please try again.')
      }
 
      const data = await response.json()
      setResponse(data["flashcards"])
      
      download("test_download.txt", data["flashcards"])

    } catch (error) {
      // Capture the error message to display to the user
      setError(error.message)
      setResponse(null)
      console.error(error)
    } finally {
      setIsLoading(false)
    }
  }

  return (
    <>
      <div style={{
        height: "100vh",
        width: "100vw"
      }}>
        <center>
          <h1 style={{ alignSelf: "end" }}>EasyFlashcards📚</h1>
        </center>
        <center>
          <h2>Create your flashcards and get ready to learn!</h2>
        </center>
        <form onSubmit={onSubmit}>
          <center>
            <textarea type="text" className={utilStyles.textarea}  placeholder={"Enter your text."} name='text'/>
          </center>
          <center>
            <button className={utilStyles.button} type="submit" disabled={isLoading}>
              {isLoading ? 'Thinking...' : 'Get my flashcards!'}
            </button>
          </center>
        </form>
        <center>
          {error && <div style={{ color: 'red' }}>{error}</div>}
        </center>
        <center>
          {response && <div style={{ color: 'green' }}>{response}</div>}
        </center>
      </div>
    </>
  );
}