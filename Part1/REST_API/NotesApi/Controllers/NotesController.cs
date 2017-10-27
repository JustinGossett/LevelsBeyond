using System.Collections.Generic;
using Microsoft.AspNetCore.Mvc;
using NotesApi.Models;
using System.Linq;

namespace NotesApi.Controllers
{
    [Route("api/[controller]")]
    public class NotesController : Controller
    {
        private readonly NotesContext _context;

        // List of notes returned for a filtered GET using the optional parameter
        // ?query=x
        private List<NotesItem> filteredNotes;

        public NotesController(NotesContext context)
        {
            _context = context;
            filteredNotes = new List<NotesItem>();

            // If there are no notes, then create a sample note
            if (_context.NotesItems.Count() == 0)
            {
                _context.NotesItems.Add(new NotesItem { Body = "Sample Note" });
                _context.SaveChanges();
            }
        }

        [HttpGet]
        public IEnumerable<NotesItem> GetAll(string query = "")
        {
            // If optional ?query=x parameter is not used,
            // then return all notes
            if (query == "")
            {
                return _context.NotesItems.ToList();
            }

            // Clear any existing notes from previous filter GET requests
            if (filteredNotes.Count() != 0)
            {
                filteredNotes.Clear();
            }

            // Add each note that satisfies filter condition to list
            foreach (NotesItem note in _context.NotesItems)
            {
                if (note.Body.Contains(query))
                {
                    filteredNotes.Add(note);
                }
            }
            return filteredNotes;
        }

        // Get note by id
        [HttpGet("{id}", Name = "GetNotes")]
        public IActionResult GetById(long id)
        {
            var item = _context.NotesItems.FirstOrDefault(t => t.Id == id);
            if (item == null)
            {
                return NotFound();
            }
            return new ObjectResult(item);
        }

        // Create and post new note
        [HttpPost]
        public IActionResult Create([FromBody] NotesItem item)
        {
            if (item == null)
            {
                return BadRequest();
            }

            _context.NotesItems.Add(item);
            _context.SaveChanges();

            return CreatedAtRoute("GetNotes", new { id = item.Id }, item);
        }

        // Update existing note by id
        [HttpPut("{id}")]
        public IActionResult Update(long id, [FromBody] NotesItem item)
        {
            var Notes = _context.NotesItems.FirstOrDefault(t => t.Id == id);
            if (Notes == null)
            {
                return NotFound();
            }

            Notes.Body = item.Body;

            _context.NotesItems.Update(Notes);
            _context.SaveChanges();
            return new NoContentResult();
        }

        // Delete existing note by id
        [HttpDelete("{id}")]
        public IActionResult Delete(long id)
        {
            var Notes = _context.NotesItems.FirstOrDefault(t => t.Id == id);
            if (Notes == null)
            {
                return NotFound();
            }

            _context.NotesItems.Remove(Notes);
            _context.SaveChanges();
            return new NoContentResult();
        }
    }
}