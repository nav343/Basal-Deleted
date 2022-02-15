import React from "react";

const Status = () => {
  return (
    <section className="text-gray-400 bg-gray-900 body-font">
      <div className="container px-5 py-24 mx-auto">
        <div className="flex flex-col text-center w-full mb-20">
          <h1 className="sm:text-3xl text-2xl font-medium title-font text-white">
            Github Status
          </h1>
          <h2 className="text-gray-400 mt-5">
            Note: The information displayed here is not updated real-time
          </h2>
        </div>
        <div className="flex flex-wrap -m-4 text-center">
          <div className="p-4 sm:w-1/4 w-1/2">
            <h2 className="title-font font-medium sm:text-4xl text-3xl text-white">
              4
            </h2>
            <p className="leading-relaxed">Stars</p>
          </div>
          <div className="p-4 sm:w-1/4 w-1/2">
            <h2 className="title-font font-medium sm:text-4xl text-3xl text-white">
              47
            </h2>
            <p className="leading-relaxed">Commits</p>
          </div>
          <div className="p-4 sm:w-1/4 w-1/2">
            <h2 className="title-font font-medium sm:text-4xl text-3xl text-white">
              0
            </h2>
            <p className="leading-relaxed">Forks</p>
          </div>
          <div className="p-4 sm:w-1/4 w-1/2">
            <h2 className="title-font font-medium sm:text-4xl text-3xl text-white">
              3
            </h2>
            <p className="leading-relaxed">Contributors</p>
          </div>
        </div>
      </div>
    </section>
  );
};

export default Status;
