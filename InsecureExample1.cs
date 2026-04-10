using System;
using System.Data.SqlClient;

class InsecureExample1
{
    public void Execute(string userInput)
    {
        string connectionString = "your_connection_string_here";
        using (SqlConnection connection = new SqlConnection(connectionString))
        {
            string query = "SELECT * FROM Users WHERE username = '" + userInput + "'";
            SqlCommand command = new SqlCommand(query, connection);
            connection.Open();
            SqlDataReader reader = command.ExecuteReader();
            // Process data here
        }
    }
}