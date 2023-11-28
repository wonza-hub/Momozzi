import { BrowserRouter, Routes, Route } from "react-router-dom";
import Refrigerator from "./routes/refrigerator/Refrigerator";
import RecipeSearcher from "./routes/search/RecipeSearcher";
import Recipe from "./routes/recipe/Recipe";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path={"refrigerator"} element={<Refrigerator />} />
        <Route path={"search"} element={<RecipeSearcher />} />
        <Route path={"recipe/:postId"} element={<Recipe />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
