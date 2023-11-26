import { BrowserRouter, Routes, Route } from "react-router-dom";
import Refrigerator from "./routes/refrigerator/Refrigerator";
import CuisineSearcher from "./routes/search/CuisineSearcher";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path={"refrigerator"} element={<Refrigerator />} />
        <Route path={"search"} element={<CuisineSearcher />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
