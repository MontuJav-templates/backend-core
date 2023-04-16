import logo from './logo.svg';
import './App.css';
import FourButtons from './modules/FourButtons';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Basic functionalities:
        </p>
        <FourButtons />
      </header>
    </div>
  );
}

export default App;
