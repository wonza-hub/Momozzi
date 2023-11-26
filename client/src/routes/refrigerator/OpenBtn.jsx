import { Button } from "@mui/material";
import axios from "axios";

const OpenBtn = ({ userId }) => {
  return (
    <>
      <button
        className="absolute bottom-12 left-2/4 -translate-x-2/4 w-36 h-12 bg-primary/90 text-xl text-white rounded-xl"
        onClick={() => {
          let openFridgeUrl = `${process.env.REACT_APP_SERVER}/userid?${userId}`;
          axios?.get(openFridgeUrl)?.then((res) => {
            // setStoredIngredients(res.data);
          });
        }}
      >
        Open
      </button>
    </>
  );
};

export default OpenBtn;
