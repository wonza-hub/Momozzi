import { BrowserRouter, Routes, Route } from "react-router-dom";
import Refrigerator from "./routes/refrigerator/Refrigerator";
import RecipeSearcher from "./routes/search/RecipeSearcher";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path={"refrigerator"} element={<Refrigerator />} />
        <Route path={"search"} element={<RecipeSearcher />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
