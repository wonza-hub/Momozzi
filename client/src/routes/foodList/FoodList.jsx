import { useLocation } from "react-router-dom";
import axios from "axios";

const FoodList = () => {
  const location = useLocation();
  const { method, category } = location.state.foodFilter;

  // let recommendUrl = `${process.env.REACT_APP_SERVER}/method?${method}category?${category}`;
  // axios?.get(recommendUrl)?.then((res) => {});
};

export default FoodList;
