const LoginModal = ({ isLoginOpen, handleLoginOpen }) => {
  return (
    <>
      <div className="absolute w-screen h-screen left-0 top-0 bg-black/80 z-20">
        <div className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[485px] h-[700px] px-4 py-8 bg-white rounded-3xl brightness-95 shadow-[0_8px_30px_rgb(0,0,0,0.12)]">
          <div className="w-full h-full flex flex-col items-center">
            <header>
              <h3 className="my-10 text-3xl text-primary tracking-wider">
                LOGIN
              </h3>
            </header>
            <div className="w-3/4">
              <form className="w-full">
                <input
                  className="w-full h-12 mb-5 px-8  bg-backgroundGray/50 rounded-lg focus:outline-primary"
                  type="text"
                  placeholder={"ID"}
                />
                <input
                  className="w-full h-12 mb-5 px-8  bg-backgroundGray/50 rounded-lg focus:outline-primary"
                  type="text"
                  placeholder={"Password"}
                />
                <button className="w-full h-12 my-5  bg-primary/90 rounded-md text-white text-lg focus:outline-primary">
                  LOGIN
                </button>
              </form>
              <div className="w-full text-center text-black/80">
                login with SNS account
              </div>
              <button className="w-full h-10 my-4 bg-kakao text-black rounded-xl">
                kakao login
              </button>
              <button className=" w-full mt-24 h-14 tracking-wider border-2 border-black/80 rounded-3xl">
                SIGN UP
              </button>
            </div>
          </div>
        </div>
      </div>
    </>
  );
};

export default LoginModal;
