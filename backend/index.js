import express from "express"
import jwt from "jsonwebtoken"
import dotenv from 'dotenv'
dotenv.config()
const app = express();
app.use(express.json());

// secret key (keep in .env in real projects)
const SECRET_KEY = process.env.SECRET_KEY;
// console.log(SECRET_KEY);
// 🛡️ MIDDLEWARE
function authMiddleware(req, res, next) {
  const authHeader = req.headers.authorization;

  if (!authHeader) {
    return res.status(401).json({ message: "Token missing" });
  }

  const token = authHeader.split(" ")[1];

  try {
    const decoded = jwt.verify(token, SECRET_KEY);
    req.user = decoded; // attach user data
    next();
  } catch (err) {
    return res.status(403).json({ message: "Invalid token" });
  }
}

// dummy user (no DB)
const user = {
  id: 1,
  username: "nency",
  password: "1234"
};


// 🔐 LOGIN ROUTE
app.post("/login", (req, res) => {
  const { username, password } = req.body;

  // basic check
  if (username !== user.username || password !== user.password) {
    return res.status(401).json({ message: "Invalid credentials" });
  }

  // create token
  const token = jwt.sign(
    { id: user.id, username: user.username },
    SECRET_KEY,
    { expiresIn: "1h" }
  );

  res.json({ token });
});





// 🔒 PROTECTED ROUTE
app.get("/protected", authMiddleware, (req, res) => {
  res.json({
    message: "You accessed protected route 🎉",
    user: req.user
  });
});


app.listen(3000, () => {
  console.log("Server running on port 3000");
}); 
