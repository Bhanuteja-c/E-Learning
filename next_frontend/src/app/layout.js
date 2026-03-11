import { Inter } from "next/font/google";
import "./globals.css";
import { AuthProvider } from "@/context/AuthContext";
import Navbar from "@/components/Navbar";

const inter = Inter({ subsets: ["latin"] });

export const metadata = {
  title: "CollabStudy",
  description: "E-Learning Platform",
};

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body className={inter.className}>
        <AuthProvider>
          <div className="app-container">
            <Navbar />
            <main style={{ minHeight: "calc(100vh - 80px)" }}>{children}</main>
          </div>
        </AuthProvider>
      </body>
    </html>
  );
}
