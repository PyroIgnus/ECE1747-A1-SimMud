#ifndef __LOG
#define __LOG

#include <fstream>
#include <string>
#include <stdint.h>

#include <SDL_thread.h>

class TSLogger{
public:
    ~TSLogger();

    static void initialize();
    static TSLogger* getInstance();

    void open(std::string filename);
    void close();

    bool write(uint32_t thread_id, uint32_t tick_count,
        uint32_t request_count, uint32_t request_time, uint32_t update_count, uint32_t update_time);

private:
    static TSLogger* instance;
    std::fstream outfile;
    SDL_sem *mutex;

    TSLogger();
};

#endif
