import { forwardRef } from "react";
import { IoIosSearch } from "react-icons/io";

/**
 * 문자열 기반 레시피 검색창 컴포넌트
 * @param {searchContent, onSearchContentChange, handleSearchBoxInputComplete}
 * @returns
 */
const SearchBox = (
  { searchContent, onSearchContentChange, handleSearchBoxInputComplete },
  ref
) => {
  return (
    <>
      <div className="relative w-60 h-12 mx-5 mt-10 my-2 overflow-hidden">
        <input
          className="w-full h-full pl-4 pr-14 rounded-2xl outline-none "
          type={"text"}
          placeholder={"레시피명을 입력하세요"}
          value={searchContent}
          onChange={onSearchContentChange}
          onKeyDown={(e) =>
            e.key === "Enter" ? handleSearchBoxInputComplete() : null
          }
          ref={ref}
        ></input>
        <button onClick={handleSearchBoxInputComplete}>
          <IoIosSearch className="absolute bottom-2 right-4 text-3xl text-black/60" />
        </button>
      </div>
    </>
  );
};

export default forwardRef(SearchBox);
