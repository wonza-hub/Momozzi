/**
 * 레시피 상세 내용 컴포넌트
 * @param {description}
 * @returns
 */
const Description = ({ description }) => {
  return (
    <>
      <header className="mb-5 text-3xl font-bold text-primary drop-shadow-sm">
        Description
      </header>
      <div className="description mb-8 font-semibold text-xl text-black/90">
        {description}
      </div>
    </>
  );
};

export default Description;
