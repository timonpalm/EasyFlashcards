import utilStyles from '../styles/Home.module.css';

export default function Home() {
  return (
    <div>
      <center>
        <h1>EasyFlashcards📚</h1>
      </center>
      <center>
        <h2>Create your flashcards and be ready to learn!</h2>
      </center>
      <center>
        <textarea className={utilStyles.textarea} placeholder={"Enter your text."} />
      </center>
      <center>
        <button className={utilStyles.button} type="submit">Get my flashcards !</button>
      </center>
    </div>
  );
}
