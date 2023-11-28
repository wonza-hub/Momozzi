const Description = ({ description }) => {
  return (
    <>
      <header className="mb-5 text-3xl font-bold text-primary drop-shadow-md">
        Description
      </header>
      <div className="description mb-8 font-semibold text-xl text-black/90">
        {description}
      </div>
    </>
  );
};

export default Description;
