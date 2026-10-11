#include <cstdio>
#include <array>
#include <iostream>
#include <boost/asio.hpp>
#include <vector>

using boost::asio::ip::tcp;
std::vector<std::string> split(std::string s, std::string delimiter) {
    size_t pos_start = 0, pos_end, delim_len = delimiter.length();
    std::string token;
    std::vector<std::string> res;

    while ((pos_end = s.find(delimiter, pos_start)) != std::string::npos) {
        token = s.substr(pos_start, pos_end - pos_start);
        pos_start = pos_end + delim_len;
        res.push_back(token);
    }

    res.push_back(s.substr (pos_start));
    return res;
}

int main(int argc, char* argv[])
{

    if (argc != 2)
    {
        std::printf("Usage: %s <host>\n", argv[0]);
        return 1;
    }
    
    std::string url = argv[1];
    
    if (url.ends_with())

    std::string protocol = "md://";
    std::vector<std::string> split_url = split(url, protocol);
    
    std::cout << split_url[1] << std::endl;

    return 69;

    try
    {
        boost::asio::io_context io_context;

        tcp::resolver resolver(io_context);
        tcp::resolver::results_type endpoints =
            resolver.resolve(argv[1], "2004");

        tcp::socket socket(io_context);
        boost::asio::connect(socket, endpoints);

        for (;;)
        {
            std::array<char, 1024> buf;
            boost::system::error_code error;

            size_t len = socket.read_some(boost::asio::buffer(buf), error);

            if (error == boost::asio::error::eof)
                break; // Connection closed cleanly by peer.
            else if (error)
                throw boost::system::system_error(error); // Some other error.

            std::cout.write(buf.data(), len);
        }
    }
    catch (std::exception& e)
    {
        std::cerr << e.what() << std::endl;
    }

    return 0;
}
