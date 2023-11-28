const Steps = ({ steps }) => {
  return (
    <>
      <header className="mb-5 text-3xl font-bold text-primary drop-shadow-md">
        Step
      </header>
      <div className="steps">
        {steps.map((step, idx) => {
          return (
            <div className="step mb-8 text-2xl flex flex-row" key={idx}>
              <div className="flex-none w-10 h-10 mr-4 pt-0.5 text-center bg-secondary text-white rounded-full">
                {idx + 1}
              </div>
              <div className="flex-initial font-semibold text-lg text-black/90 tracking-wide leading-loose">
                {step}
              </div>
            </div>
          );
        })}
      </div>
    </>
  );
};

export default Steps;
