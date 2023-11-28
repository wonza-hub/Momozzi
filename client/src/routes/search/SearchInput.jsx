import { forwardRef } from "react";

const SearchInput = ({ searchContent, onSearchContentChange }, ref) => {
  return (
    <>
      <input
        className="w-60 h-12 mx-5 my-2 px-6 text-xl font-bold rounded-2xl"
        type={"text"}
        placeholder={"Cuisine name"}
        value={searchContent}
        onChange={onSearchContentChange}
        ref={ref}
      ></input>
    </>
  );
};

export default forwardRef(SearchInput);
