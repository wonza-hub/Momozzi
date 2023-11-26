import axios from "axios";

const OpenBtn = ({ userId }) => {
  return (
    <>
      <button
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
