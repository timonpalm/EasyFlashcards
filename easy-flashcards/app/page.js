"use client";
import React, { useState } from 'react'
import utilStyles from './page.module.css';

export default function Home() {
  const [isLoading, setIsLoading] = useState(false)
  const [error, setError] = useState(null)

  async function onSubmit(e) {
    e.preventDefault();
    setIsLoading(true);
    setError(null)

    const formData = new FormData(e.currentTarget);
    console.log(formData.get('text'));

  //   try {
  //     const response = await fetch('/api/submit', {
  //       method: 'POST',
  //       body: formData,
  //     })
 
  //     if (!response.ok) {
  //       throw new Error('Failed to submit the data. Please try again.')
  //     }
 
  //     const data = await response.json()
  //     // ...
  //   } catch (error) {
  //     // Capture the error message to display to the user
  //     setError(error.message)
  //     console.error(error)
  //   } finally {
  //     setIsLoading(false)
  //   }
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
              {isLoading ? 'Loading...' : 'Get my flashcards!'}
            </button>
          </center>
        </form>
        <center>
          {error && <div style={{ color: 'red' }}>{error}</div>}
        </center>
      </div>
    </>
  );
}