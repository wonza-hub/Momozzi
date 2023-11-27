import SearchBar from "./SearchBar";
import CuisineList from "./CuisineList";
import { useEffect, useState } from "react";
import { useLocation } from "react-router-dom";
import axios from "axios";

const CuisineSearcher = () => {
  const location = useLocation();
  const foodFilter = location.state && location.state.foodFilter;
  const { method, category } = foodFilter || {};

  const [cuisines, setCuisines] = useState([]);

  useEffect(() => {
    if (method || category) {
      const recommendUrl = `${process.env.REACT_APP_SERVER}/`;
      axios?.get(recommendUrl)?.then((res) => {
        setCuisines(res.data);
      });
    } else {
      const dataUrl = `${process.env.REACT_APP_SERVER}/`;
      axios?.get(dataUrl)?.then((res) => {
        setCuisines(res.data);
      });
    }
  }, [method, category]);

  return (
    <>
      <SearchBar setCuisines={setCuisines}></SearchBar>
      <CuisineList cuisines={cuisines}></CuisineList>
    </>
  );
};

export default CuisineSearcher;
