import { BrowserRouter, Routes, Route } from "react-router-dom";
import NavBar from "./components/NavBar";
import Refrigerator from "./routes/refrigerator/Refrigerator";
import RecipeSearcher from "./routes/search/RecipeSearcher";
import RecipeRecommendation from "./routes/recommend/RecipeRecommendation";
import Recipe from "./routes/recipe/Recipe";
import Mypage from "./routes/mypage/Mypage";
import MainPage from "./routes/main/MainPage";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path={"/"} element={<NavBar />}>
          <Route path={""} element={<MainPage />} />
          <Route path={"mypage"} element={<Mypage />} />
          <Route path={"refrigerator/:fridgeId"} element={<Refrigerator />} />
          <Route path={"search"} element={<RecipeSearcher />} />
          <Route path={"recommend"} element={<RecipeRecommendation />} />
          <Route path={"recipe/:postId"} element={<Recipe />} />
        </Route>
      </Routes>
    </BrowserRouter>
  );
}

export default App;
