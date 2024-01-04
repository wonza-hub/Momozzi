import { useEffect } from "react";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import { useDispatch } from "react-redux";
import { loadUser } from "./reducer/userReducer";
import NavBar from "./components/NavBar";
import Refrigerator from "./routes/refrigerator/Refrigerator";
import RecipeSearch from "./routes/search/RecipeSearch";
import Recipe from "./routes/recipe/Recipe";
import Mypage from "./routes/mypage/Mypage";
import MainPage from "./routes/main/MainPage";

function App() {
  const userDispatch = useDispatch();
  useEffect(() => {
    userDispatch(loadUser());
  }, [userDispatch]);

  return (
    <BrowserRouter>
      <Routes>
        <Route path={"/"} element={<NavBar />}>
          <Route path={""} element={<MainPage />} />
          <Route path={"mypage"} element={<Mypage />} />
          <Route path={"refrigerator/:fridgeId"} element={<Refrigerator />} />
          <Route path={"search"} element={<RecipeSearch />} />
          <Route path={"recipe/:postId"} element={<Recipe />} />
        </Route>
      </Routes>
    </BrowserRouter>
  );
}

export default App;
