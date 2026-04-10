using System;

class InsecureExample2
{
    private const string hardcodedUsername = "admin";
    private const string hardcodedPassword = "password123"; // Weak password

    public static void Main(string[] args)
    {
        string inputUsername = hardcodedUsername;
        string inputPassword = hardcodedPassword;

        // Simulating user login
        if (Login(inputUsername, inputPassword))
        {
            Console.WriteLine("Login successful!");
        }
        else
        {
            Console.WriteLine("Login failed!");
        }
    }

    private static bool Login(string username, string password)
    {
        // Insecure password check
        return username == hardcodedUsername && password == hardcodedPassword;
    }
}