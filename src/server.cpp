#include <cstdio>
#include <ctime>
#include <iostream>
#include <string_view>
#include <boost/asio.hpp>

using boost::asio::ip::tcp;

constexpr int MDP_MAJOR = 1;
constexpr int MDP_MINOR = 0;
constexpr int MDP_PATCH = 0;
constexpr char* MDP_STRING = "a";

char* get_time()
{
    std::time_t now = std::time(0);
    return std::ctime(&now);
}

int main()
{
    char version[20];
    std::sprintf(version, "v%d.%d.%d%s", MDP_MAJOR, MDP_MINOR, MDP_PATCH, MDP_STRING);

    try
    {
        boost::asio::io_context io_context;

        tcp::acceptor acceptor(io_context, tcp::endpoint(tcp::v4(), 2004));

        for (;;)
        {
            tcp::socket socket(io_context);
            acceptor.accept(socket);

            char message[1024];

            std::sprintf(message, "md:// version %s\n\nHello from md:// server!\nThe server currently does not provide any content\nTime: %s", version, get_time());
    
            boost::system::error_code ignored_error;
            boost::asio::write(socket, boost::asio::buffer(std::string_view(message)), ignored_error);
        }
    }
    catch (std::exception& e)
    {
        std::cerr << e.what() << std::endl;
    }

    return 0;
}


