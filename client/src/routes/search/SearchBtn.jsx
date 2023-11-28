const SearchBtn = ({ handleSearchClick }) => {
  return (
    <>
      <button
        className="bg-primary/80 text-white text-2xl font-bold w-60 h-12 mx-5 my-2 rounded-2xl"
        onClick={handleSearchClick}
      >
        Search
      </button>
    </>
  );
};

export default SearchBtn;
