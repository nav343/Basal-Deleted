import React from "react";
import Documentation from "../components/Documentation";
import Footer from "../components/Footer";
import Header from "../components/Header";

export default function Docs() {
  document.title = "Basal - Docs";
  return (
    <>
      <Header />
      <Documentation />
      <Footer />
    </>
  );
}
