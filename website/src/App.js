import "./App.css";
import Home from "./pages/Home";
import Download from "./pages/Download";
import Docs from "./pages/Docs";
import _404 from "./pages/404";
import { BrowserRouter, Route, Routes } from "react-router-dom";

function App() {
  return (
    <div className="App">
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/download" element={<Download />} />
          <Route path="/docs" element={<Docs />} />
          <Route path="/*" element={<_404 />} />
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;
