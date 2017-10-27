using Microsoft.EntityFrameworkCore;
using System.Collections.Generic;

namespace NotesApi.Models
{
    // Class for creating the database context
    public class NotesContext : DbContext
    {
        public NotesContext(DbContextOptions<NotesContext> options)
            : base(options)
        {
        }

        public DbSet<NotesItem> NotesItems { get; set; }
    }
}