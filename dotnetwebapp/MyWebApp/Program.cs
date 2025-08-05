var builder = WebApplication.CreateBuilder(args);
var app = builder.Build();

app.MapGet("/", () => "Hello World!");

app.MapGet("/secret", (string? password) =>
{
    if (password == "supersecret"){
        return "You have accessed the secret!";
    }
    else {
        return "Access denied!";
    }
});

app.Run();
