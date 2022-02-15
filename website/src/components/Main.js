import React from "react";
import { Link } from "react-router-dom";
import Tilt from "react-tilt";

export default function Main() {
  return (
    <section className="text-gray-400 bg-gray-900 body-font">
      <div className="container mx-auto flex px-5 py-24 md:flex-row flex-col items-center">
        <Tilt className="Tilt" options={{ max: 25 }}>
          <div className="lg:max-w-lg lg:w-full md:w-1/2 w-5/6 mb-10 md:mb-0 Tilt-inner">
            <img
              className="object-cover object-center rounded ml-5"
              alt="hero"
              src="https://images.unsplash.com/photo-1587620962725-abab7fe55159?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1031&q=80"
              draggable="false"
              ref={React.createRef()}
            />
          </div>
        </Tilt>
        <div className="lg:flex-grow md:w-1/2 lg:pl-24 md:pl-16 flex flex-col md:items-start md:text-left items-center text-center">
          <h1 className="title-font sm:text-4xl text-3xl mb-4 font-medium text-white">
            Get Started with Basal
          </h1>
          <p className="mb-8 leading-relaxed">
            A general purpose low level programming language written in Python.
            Basal is an easy mid level programming language compiling to C. It
            has an easy syntax, similar to Python, Rust etc.
          </p>
          <div className="flex justify-center mb-6">
            <Link
              to="/docs"
              className="inline-flex text-white bg-indigo-500 border-0 py-2 px-6 focus:outline-none hover:bg-indigo-600 rounded text-lg"
            >
              Get Started
            </Link>
            <a
              href="https://github.com/SnmLogic/Basal/"
              target="_blank"
              className="ml-4 inline-flex text-gray-400 bg-gray-800 border-0 py-2 px-6 focus:outline-none hover:bg-gray-700 hover:text-white rounded text-lg"
            >
              Github
            </a>
          </div>
          <div className="flex lg:flex-row md:flex-col text-gray-300">
            <Link
              to="/download"
              className="bg-gray-800 inline-flex py-3 px-5 rounded-lg items-center hover:bg-gray-700 hover:text-white focus:outline-none"
            >
              <img
                src="https://img.icons8.com/ios-filled/50/ffffff/windows-10.png"
                alt="Windows Logo"
                className="w-9 h-9"
                ref={React.createRef()}
                draggable="false"
              />
              <span className="ml-4 flex items-start flex-col leading-none">
                <span className="text-xs text-gray-400 mb-1">Get it for</span>
                <span className="title-font font-medium">Windows</span>
              </span>
            </Link>
            <Link
              to="/download"
              className="bg-gray-800 inline-flex py-3 px-5 rounded-lg items-center hover:bg-gray-700 hover:text-white focus:outline-none lg:ml-4 md:ml-0 ml-4 md:mt-4 mt-0 lg:mt-0"
            >
              <img
                src="https://img.icons8.com/ios-filled/50/ffffff/mac-os.png"
                alt="Windows Logo"
                className="w-9 h-9"
                ref={React.createRef()}
                draggable="false"
              />
              <span className="ml-4 flex items-start flex-col leading-none">
                <span className="text-xs text-gray-400 mb-1">Get it for</span>
                <span className="title-font font-medium">Mac</span>
              </span>
            </Link>
          </div>
        </div>
      </div>
    </section>
  );
}
