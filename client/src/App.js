import { BrowserRouter, Routes, Route } from "react-router-dom";
import NavBar from "./components/NavBar";
import Refrigerator from "./routes/refrigerator/Refrigerator";
import RecipeSearcher from "./routes/search/RecipeSearcher";
import RecipeRecommendation from "./routes/recommend/RecipeRecommendation";
import Recipe from "./routes/recipe/Recipe";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path={"/"} element={<NavBar />}>
          <Route path={"refrigerator"} element={<Refrigerator />} />
          <Route path={"search"} element={<RecipeSearcher />} />
          <Route path={"recommend"} element={<RecipeRecommendation />} />
          <Route path={"recipe/:postId"} element={<Recipe />} />
        </Route>
      </Routes>
    </BrowserRouter>
  );
}

export default App;
