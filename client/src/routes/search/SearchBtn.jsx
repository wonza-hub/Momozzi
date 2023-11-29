const SearchBtn = ({ handleSearchClick }) => {
  return (
    <>
      <button
        className="text-white text-xl font-bold w-60 h-12 mx-5 my-1 bg-primary/80 rounded-2xl hover:bg-primary/90 duration-300"
        onClick={handleSearchClick}
      >
        Search
      </button>
    </>
  );
};

export default SearchBtn;
