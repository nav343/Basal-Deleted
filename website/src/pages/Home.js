import React from "react";
import Status from "../components/Status";
import Features from "../components/Features";
import Header from "../components/Header";
import Main from "../components/Main";
import Footer from "../components/Footer";

export default function Home() {
  document.title = "Basal - Home";
  return (
    <>
      <Header />
      <Main />
      <Features />
      <Status />
      <Footer />
    </>
  );
}
