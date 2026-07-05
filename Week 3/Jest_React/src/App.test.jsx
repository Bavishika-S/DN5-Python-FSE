import { render, screen, fireEvent } from "@testing-library/react";
import { describe, test, expect } from "vitest";
import App from "./App";

describe("App Component", () => {
  test("renders heading", () => {
    render(<App />);
    expect(screen.getByText("React Testing Demo")).toBeInTheDocument();
  });

  test("increments counter", () => {
    render(<App />);

    fireEvent.click(screen.getByText("Increment"));

    expect(screen.getByTestId("count")).toHaveTextContent("1");
  });
});