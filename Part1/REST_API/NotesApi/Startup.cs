using Microsoft.AspNetCore.Builder;
using Microsoft.EntityFrameworkCore;
using Microsoft.Extensions.DependencyInjection;
using NotesApi.Models;

namespace NotesApi
{
    public class Startup
    {
        public void ConfigureServices(IServiceCollection services)
        {
            // Register the database context
            services.AddDbContext<NotesContext>(opt => opt.UseInMemoryDatabase("NotesList"));
            services.AddMvc();
        }

        public void Configure(IApplicationBuilder app)
        {
            app.UseMvc();
        }
    }
}