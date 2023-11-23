import { BrowserRouter, Routes, Route } from "react-router-dom";
import Refrigerator from "./routes/refrigerator/Refrigerator";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path={"refrigerator"} element={<Refrigerator />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
