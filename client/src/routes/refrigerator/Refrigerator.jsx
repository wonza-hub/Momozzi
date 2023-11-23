import Inventory from "./Inventory";
import DropDown from "../../components/DropDown";
import { METHOD, CATEGORY } from "../../constants/Constant";
import { useState } from "react";
import { useNavigate } from "react-router-dom";

const Refrigerator = () => {
  const [method, setMethod] = useState("");
  const [category, setCategory] = useState("");

  const navigate = useNavigate();

  return (
    <>
      <Inventory></Inventory>
      <div>
        <div>
          <span>Method</span>
          <DropDown menuItems={METHOD} setArg={setMethod}></DropDown>
        </div>
        <div>
          <span>Category</span>
          <DropDown menuItems={CATEGORY} setArg={setCategory}></DropDown>
        </div>
      </div>
      <button
        onClick={() => {
          navigate("/search", {
            state: {
              metaData: {
                method,
                category,
              },
            },
          });
        }}
      >
        Recommend!
      </button>
    </>
  );
};

export default Refrigerator;
