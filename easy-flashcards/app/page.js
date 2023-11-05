"use client";

import utilStyles from './Home.module.css';
import { useState } from "react"

export default function Home() {

  function handleSubmit(e) {
    const form = e.target;
    const formData = new FormData(form);
    console.log(formData)
    //alert(str + " i did it");
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
          <form method="post" onSubmit={handleSubmit}>
          <center>
            <textarea className={utilStyles.textarea}  placeholder={"Enter your text."} onChange={(e) => {
              //setInputText(e.target.value)
              //console.log(inputText)
            }} />
          </center>
          <center>
            <button className={utilStyles.button} type="submit" onSubmit={(e) => {
              txt = getText()
              console.log(text)
            }}>Get my flashcards !</button>
          </center>
        </form>
      </div>
    </>
  );
}