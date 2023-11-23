import { BrowserRouter, Routes, Route } from "react-router-dom";
import Refrigerator from "./routes/refrigerator/Refrigerator";
import FoodList from "./routes/foodList/FoodList";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path={"refrigerator"} element={<Refrigerator />} />
        <Route path={"foodList"} element={<FoodList />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
